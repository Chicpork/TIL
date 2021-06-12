import React from "react";
import PropTypes from "prop-types";

const foodILike = [
  {
    id:1,
    name: "kimchi",
    image: "https://w.namu.la/s/2958e0d7304f1b744021983c55747de2840e0e59a1f3d677d9315f5bad981f002769ce59921aea02b2dd23b5384a0ce30864fe6d84ea1b9aaed80fb3b5f60b6d21e9a769219133171d83c048784a8fb2ba6cb3c5588d66502749375b8ea62144d02c7ac26d20b10b09c5a0b3d70dacf8",
    rating: 5.5
  },
  {
    id:2,
    name: "kimbab",
    image: "https://recipe1.ezmember.co.kr/cache/recipe/2016/02/21/f34c2f0fcd67513941d683d90050f3c01.jpg",
    rating: 4.7
  }
]

function Food({name, picture, rating}) {
  return <div>
    <h2>I like {name}</h2>
    <h4>{rating}/5.0</h4>
    <img src={picture} alt={name}/>
  </div>;
}

Food.propTypes = {
  name: PropTypes.string.isRequired,
  picture: PropTypes.string.isRequired,
  rating: PropTypes.number
}

function App() {
  return (
    <div className="App">
      {foodILike.map(dish => (
        <Food key={dish.id} name={dish.name} picture={dish.image} rating={dish.rating}/>
      ))}
    </div>
  );
}

export default App;
