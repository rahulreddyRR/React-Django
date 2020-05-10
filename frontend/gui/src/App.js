import React from 'react';
import {BrowserRouter as Router} from 'react-router-dom';
import BaseRouter from './routes';

import 'antd/dist/antd.css';
import Customlayout from './containers/Layout';

function App() {
  return (
    <div className="App">
      <Router>
      <Customlayout>
          <BaseRouter/>
      </Customlayout>
      </Router>
      
    </div>
  );
}

export default App;
