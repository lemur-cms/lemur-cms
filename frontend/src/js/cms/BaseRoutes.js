import React from "react";
import { Link, Route, Switch} from "react-router-dom";
import axios from "axios";
import Page from "./Page";

class BaseRoutes extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      pages: [],
    };
  }

  refreshList = () => {
    axios
      .get(`http://localhost:8000/api/pages/`)
      .then(res => this.setState({ pages: res.data}))
      .catch(err => console.log(err));
  }

  UsersPage = () => {
    return (
      <>
        <h3>Users Page</h3>
        {this.state.pages.map((page, index) => (
          <h5 key={index}>
            <Link to={`${page._cached_url}`}>{page.title}</Link>
          </h5>
        ))}
      </>
    );
  };

  componentDidMount() {
    this.refreshList();
  }

  IndexPage = (id) => {
    return <Page pageID={id}/>;
  };

  NoMatchPage = () => {
    return <h1>404</h1>;
  };

  render() {
    return (
    <React.Fragment>
      <Switch>
        <Route exact path="/pages" component={this.UsersPage} />
        {this.state.pages.map((page, index) => (
          <Route key={index} exact path={page._cached_url} component={() => this.IndexPage(page.id)}/>
        ))}
        <Route component={this.NoMatchPage} />
      </Switch>
    </React.Fragment>
    )
  }
}

export default BaseRoutes;
