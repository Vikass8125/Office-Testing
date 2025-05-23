import { useState } from 'react';
import './UserForm.css';

const UserForm = () => {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: ''
  });
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setMessage('');

    try {
      const response = await fetch('/api/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setMessage('User details saved successfully!');
        setFormData({ first_name: '', last_name: '' });
      } else {
        setMessage('Error saving user details. Please try again.');
      }
    } catch (error) {
      setMessage('Error connecting to the server. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="user-form-container">
      <h2>User Details</h2>
      <form onSubmit={handleSubmit} className="user-form">
        <div className="form-group">
          <label htmlFor="first_name">First Name:</label>
          <input
            type="text"
            id="first_name"
            name="first_name"
            value={formData.first_name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="last_name">Last Name:</label>
          <input
            type="text"
            id="last_name"
            name="last_name"
            value={formData.last_name}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Saving...' : 'Submit'}
        </button>
      </form>
      {message && <div className={`message ${message.includes('Error') ? 'error' : 'success'}`}>
        {message}
      </div>}
    </div>
  );
};

export default UserForm; 