import React from 'react';
import RiskGauge from './components/RiskGauge';
import IOCGraph from './components/IOCGraph';
import Leaderboard from './components/Leaderboard'; // Gamified Unique
import ForecastChart from './components/ForecastChart'; // Predictive Unique

function App() {
  return (
    <div>
      <h1>Email Security Dashboard</h1>
      <RiskGauge score={75} />
      <IOCGraph data={/* fetch from API */} />
      <Leaderboard users={/* analyst scores */} />
      <ForecastChart trends={/* prophet output */} />
    </div>
  );
}

export default App;