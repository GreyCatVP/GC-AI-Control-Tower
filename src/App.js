import React from 'react';
import { Tabs, Tab } from 'react-bootstrap';
import CostTab from './components/CostTab';
import RiskTab from './components/RiskTab';
import AccessTab from './components/AccessTab';

function App() {
  return (
    <Tabs defaultActiveKey="cost" id="control-tower-tabs">
      <Tab eventKey="cost" title="💰 Cost">
        <CostTab />
      </Tab>
      <Tab eventKey="risk" title="🔐 Risk">
        <RiskTab />
      </Tab>
      <Tab eventKey="access" title="🧑‍💼 Access">
        <AccessTab />
      </Tab>
    </Tabs>
  );
}

export default App;
