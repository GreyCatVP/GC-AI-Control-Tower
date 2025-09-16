import React, { useState } from 'react';
import axios from 'axios';

function AccessTab() {
  const [username, setUsername] = useState('');

  const handleOffboard = async () => {
    const res = await axios.post(`/access/offboard?username=${username}`);
    alert(res.data.message);
  };

  return (
    <div>
      <h3>Access Control</h3>
      <input type="text" placeholder="username" onChange={(e) => setUsername(e.target.value)} />
      <button onClick={handleOffboard}>Отключить всё</button>
    </div>
  );
}

export default AccessTab;
