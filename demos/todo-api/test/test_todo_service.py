import unittest
from unittest.mock import patch, MagicMock
from service.todo_service import create_todo


class TestCreateTodo(unittest.TestCase):
    
    @patch('service.todo_service.create_todo_record')
    def test_create_todo_success(self, mock_create):
        """Test successful todo creation"""
        mock_todo = MagicMock(id=1, title="Buy groceries", description="Milk and eggs")
        mock_create.return_value = mock_todo
        
        data = {"title": "Buy groceries", "description": "Milk and eggs"}
        todo, error = create_todo(data)
        
        self.assertIsNotNone(todo)
        self.assertIsNone(error)
        self.assertEqual(todo.title, "Buy groceries")
        mock_create.assert_called_once_with("Buy groceries", "Milk and eggs")
    
    def test_create_todo_missing_title(self):
        """Test creation fails when title is empty"""
        data = {"title": "", "description": "Some description"}
        todo, error = create_todo(data)
        
        self.assertIsNone(todo)
        self.assertEqual(error, "Title is required")
    
    def test_create_todo_title_whitespace_only(self):
        """Test creation fails when title is only whitespace"""
        data = {"title": "   ", "description": "Some description"}
        todo, error = create_todo(data)
        
        self.assertIsNone(todo)
        self.assertEqual(error, "Title is required")
    
    def test_create_todo_invalid_title_type(self):
        """Test creation fails when title is not a string"""
        data = {"title": 123, "description": "Some description"}
        todo, error = create_todo(data)
        
        self.assertIsNone(todo)
        self.assertEqual(error, "Title must be text")
    
    def test_create_todo_invalid_description_type(self):
        """Test creation fails when description is not a string"""
        data = {"title": "Valid Title", "description": 456}
        todo, error = create_todo(data)
        
        self.assertIsNone(todo)
        self.assertEqual(error, "Description must be text")
    
    @patch('service.todo_service.create_todo_record')
    def test_create_todo_strips_whitespace(self, mock_create):
        """Test that title and description are trimmed"""
        mock_todo = MagicMock(id=2, title="Test", description="Description")
        mock_create.return_value = mock_todo
        
        data = {"title": "  Test  ", "description": "  Description  "}
        todo, error = create_todo(data)
        
        self.assertIsNone(error)
        mock_create.assert_called_once_with("Test", "Description")
    
    @patch('service.todo_service.create_todo_record')
    def test_create_todo_empty_description_allowed(self, mock_create):
        """Test that empty description is allowed"""
        mock_todo = MagicMock(id=3, title="Task", description="")
        mock_create.return_value = mock_todo
        
        data = {"title": "Task", "description": ""}
        todo, error = create_todo(data)
        
        self.assertIsNone(error)
        self.assertIsNotNone(todo)
        mock_create.assert_called_once_with("Task", "")
    
    def test_create_todo_missing_data_keys(self):
        """Test creation with missing keys defaults to empty strings"""
        data = {}
        todo, error = create_todo(data)
        
        self.assertIsNone(todo)
        self.assertEqual(error, "Title is required")


if __name__ == '__main__':
    unittest.main()
