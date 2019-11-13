import React, { Component } from "react";
import { connect } from "react-redux";
import { getData } from "../actions/index";
import {Link} from "react-router-dom";

export class Post extends Component {
  componentDidMount() {
    this.props.getData();
  }
  render() {
    return (
      <ul>
        {this.props.articles.map((page, index) => (
          <li key={index}><Link to={page._cached_url}>{page.title}</Link></li>
        ))}
      </ul>
    );
  }
}
function mapStateToProps(state) {
  return {
    articles: state.remoteArticles.slice(0, 10)
  };
}

export default connect(
  mapStateToProps,
  { getData }
)(Post);
