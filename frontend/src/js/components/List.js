import React from "react";
import { connect } from "react-redux";

const mapStateToProps = (state) => {
  return { articles: state.articles };
};

const connectedList = ({articles}) => (
  <ul>
    {articles.map((el, index) => (
      <li key={index}>{el.title}</li>
    ))}
  </ul>
);

const List = connect(mapStateToProps)(connectedList);

export default List;
