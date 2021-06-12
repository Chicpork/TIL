import React from 'react';
import { Link } from 'react-router-dom';
import './Navigation.css';

function Navigation() {
  return (
    <div>
      <Link className="navi_link" to="/">
        Home
      </Link>
      <Link className="navi_link" to="/about">
        About
      </Link>
      <Link className="navi_link" to="/movie">
        Movie
      </Link>
      <Link className="navi_link" to="/signin">
        Signin
      </Link>
    </div>
  );
}

export default Navigation;
