import React from "react";
import { connect } from "react-redux";
import { addArticle } from "../actions";

const mapDispatchToProps = (dispatch) => {
  return {
    addArticle: (article) => dispatch(addArticle(article)),
  }
};

class connectedForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      title: ""
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  handleChange(e) {
    this.setState({ [e.target.id]: e.target.value })
  }
  handleSubmit(e) {
    e.preventDefault();
    const { title } = this.state;
    this.props.addArticle({ title })
    this.setState({ title: "" })
  }
  render() {
    const { title } = this.state;
    return (
      <form onSubmit={this.handleSubmit}>
        <div>
          <label htmlFor="title">Title</label>
          <input type="text" id="title" value={title} onChange={this.handleChange} required/>
        </div>
        <button type="submit">Save</button>
      </form>
    );
  }
}

const Form = connect(null, mapDispatchToProps)(connectedForm);

export default Form;
