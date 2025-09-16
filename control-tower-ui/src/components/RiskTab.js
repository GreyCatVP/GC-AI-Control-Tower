import React, { useState } from 'react';
import axios from 'axios';

function RiskTab() {
  const [policy, setPolicy] = useState({
    who: "юристы",
    what: "не видят",
    where: "HR-документы"
  });

  const handleApply = async () => {
    const res = await axios.post('/risk/apply', policy);
    alert(res.data.message);
  };

  return (
    <div>
      <h3>Policy Builder</h3>
      <p>Кто: {policy.who}</p>
      <p>Что: {policy.what}</p>
      <p>Где: {policy.where}</p>
      <button onClick={handleApply}>Применить</button>
    </div>
  );
}

export default RiskTab;
