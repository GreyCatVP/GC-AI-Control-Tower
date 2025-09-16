import React, { useEffect, useState } from 'react';
import axios from 'axios';

function CostTab() {
  const [report, setReport] = useState(null);

  useEffect(() => {
    axios.get('/cost/report?dept=R&D&days=30').then(res => setReport(res.data));
  }, []);

  if (!report) return <p>Loading...</p>;

  return (
    <div>
      <h3>💰 Cost Report</h3>
      <p>Cost per 1k tokens: ${report.cost_per_1k_tokens}</p>
      <p>Latency p95: {report.latency_p95_ms} ms</p>
      <p>Cache hit rate: {(report.cache_hit_rate * 100).toFixed(1)}%</p>
      <p>Quota burn: {report.quota_burn_percent}%</p>
      <p><strong>Recommendation:</strong> {report.recommendation}</p>
    </div>
  );
}

export default CostTab;
