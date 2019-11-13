import React from 'react';
import ReactDOM from 'react-dom';
import { Link, BrowserRouter as Router } from "react-router-dom";
import { Layout, Menu, Breadcrumb, Icon, Row, Col } from 'antd';
import { Provider } from "react-redux";
import BaseRoutes from "./js/cms/BaseRoutes";
import * as serviceWorker from './serviceWorker';
import './index.css';
import store from "./js/store";

const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout;

ReactDOM.render(
  <Provider store={store}>
    <Router>
      <BaseRoutes/>
    </Router>
  </Provider>,
  document.getElementById('lemur-cms'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
