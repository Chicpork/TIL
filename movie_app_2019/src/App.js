import React from 'react';
import { HashRouter, Route } from 'react-router-dom';
import About from './routes/About';
import MovieHome from './routes/MovieHome';
import Detail from './routes/Detail';
import SignIn from './routes/SignIn';
import SignUp from './routes/SignUp';
import Navigation from './components/Navigation';

function App() {
  return (
    <HashRouter>
      <Navigation />
      <Route path="/movie" exact={true} component={MovieHome} />
      <Route path="/about" component={About} />
      <Route path="/movie/:id" component={Detail} />
      <Route path="/signin" component={SignIn} />
      <Route path="/signup" component={SignUp} />
    </HashRouter>
  );
}

export default App;
