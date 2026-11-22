import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from etl import extract_csv, transform_rows


class EtlCsvTests(unittest.TestCase):
    def test_utf8_csv_with_or_without_bom_cleans_the_same_customer(self):
        csv_text = (
            "first_name,last_name,email,country,signup_date,is_active,notes\r\n"
            'Élodie,Díaz,elodie@example.test,España,2026-01-02,true,"Comma, preserved"\r\n'
        )
        for encoding in ("utf-8", "utf-8-sig"):
            with self.subTest(encoding=encoding), TemporaryDirectory() as directory:
                source = Path(directory) / "customers.csv"
                source.write_bytes(csv_text.encode(encoding))
                rows = extract_csv(source)
                cleaned, rejected = transform_rows(rows)

                self.assertEqual(rejected, [])
                self.assertEqual(len(cleaned), 1)
                self.assertEqual(cleaned[0]["first_name"], "Élodie")
                self.assertEqual(cleaned[0]["last_name"], "Díaz")
                self.assertEqual(cleaned[0]["country"], "España")
                self.assertEqual(cleaned[0]["notes"], "Comma, preserved")

    def test_short_rows_do_not_abort_transform(self):
        with TemporaryDirectory() as directory:
            source = Path(directory) / "customers.csv"
            source.write_text(
                "first_name,last_name,email,country,signup_date,is_active,notes\n"
                " Ada ,EXAMPLE, ADA@example.test ,,2026-01-02,true\n"
                "Missing,Email\n"
                "Grace,Example,grace@example.test,united states,2026-01-03,true,Valid row\n",
                encoding="utf-8",
            )
            rows = extract_csv(source)
            self.assertIsNone(rows[0]["notes"])
            self.assertIsNone(rows[1]["email"])
            cleaned, rejected = transform_rows(rows)

        self.assertEqual([row["email"] for row in cleaned], ["ada@example.test", "grace@example.test"])
        self.assertEqual(cleaned[0]["first_name"], "Ada")
        self.assertIsNone(cleaned[0]["country"])
        self.assertIsNone(cleaned[0]["notes"])
        self.assertEqual(cleaned[1]["country"], "United States")
        self.assertEqual(cleaned[1]["notes"], "Valid row")
        self.assertEqual(len(rejected), 1)
        self.assertEqual(rejected[0]["first_name"], "Missing")
        self.assertEqual(rejected[0]["error"], "Missing required fields or invalid email")

    def test_omitted_optional_fields_stay_none(self):
        with TemporaryDirectory() as directory:
            source = Path(directory) / "customers.csv"
            source.write_text(
                "first_name,last_name,email,signup_date,is_active,country,notes\n"
                "Synthetic,Sample,synthetic@example.test,2026-01-02,true\n",
                encoding="utf-8",
            )
            rows = extract_csv(source)
            self.assertIsNone(rows[0]["country"])
            self.assertIsNone(rows[0]["notes"])
            cleaned, rejected = transform_rows(rows)

        self.assertEqual(rejected, [])
        self.assertEqual(len(cleaned), 1)
        self.assertIsNone(cleaned[0]["country"])
        self.assertIsNone(cleaned[0]["notes"])
