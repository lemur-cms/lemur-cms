import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import TodoApp from './TodoApp';
import ServiceApp from './ServiceApp'
import * as serviceWorker from './serviceWorker';
import { Layout, Menu, Breadcrumb, Icon, Row, Col } from 'antd';
const { SubMenu } = Menu;

//ReactDOM.render(<TodoApp />, document.getElementById('todo-app'));
const { Header, Content, Sider } = Layout;

ReactDOM.render(
  <Layout>
    <Header className="header">
      <div className="logo" />
      <Menu
        theme="dark"
        mode="horizontal"
        defaultSelectedKeys={['1']}
        style={{ lineHeight: '64px' }}
      >
        <Menu.Item key="1">Home</Menu.Item>
      </Menu>
    </Header>
    <Layout>
      <Sider width={200} style={{ background: '#fff' }}>
        <Menu
          mode="inline"
          defaultSelectedKeys={['1']}
          defaultOpenKeys={['sub1']}
          style={{ height: '100%', borderRight: 0 }}
        >
          <SubMenu
            key="sub1"
            title={
              <span>
                <Icon type="user" />
                More
              </span>
            }
          >
            <Menu.Item key="1">About</Menu.Item>
            <Menu.Item key="2">Contact</Menu.Item>
          </SubMenu>
        </Menu>
      </Sider>
      <Layout style={{ padding: '0 24px 24px' }}>
        <Breadcrumb style={{ margin: '16px 0' }}>
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item>List</Breadcrumb.Item>
          <Breadcrumb.Item>App</Breadcrumb.Item>
        </Breadcrumb>
        <Content>
          <Row>
              <Col span={24}>
                <ServiceApp/>
              </Col>
          </Row>
        </Content>
      </Layout>
    </Layout>
  </Layout>,
  document.getElementById('pages-app'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
