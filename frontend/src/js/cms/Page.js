import React from "react";
import { Link } from "react-router-dom";
import ReactSafeHtml from "react-safe-html";
import { Layout, Menu, Breadcrumb, Icon } from 'antd';
import List from "../components/List";
import Form from "../components/Form";
import Post from "../components/Posts";
import { connect } from "react-redux";
import { getPageData } from "../actions/index";

const { SubMenu } = Menu;

const { Header, Content, Sider } = Layout;

class Page extends React.Component {
  _isMounted = false;

  constructor(props) {
    super(props);
    this.state = {
      currPage: [],
      pageLoaded: false,
      mounted: false
    };
  }

  componentDidMount() {
    this.props.getPageData(this.props.pageID);
    this._isMounted = true;
  }

  componentWillUnmount() {
    this._isMounted = false;
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

  footer = (page) => {
    return (
      <React.Fragment>
        <h1>HELLO</h1>
        <h3>{page.title}</h3>


        {page.regions.footer.map((widget, index) => (
          <React.Fragment key={index}>
            <ReactSafeHtml html={widget.content} />
          </React.Fragment>
        ))}
      </React.Fragment>
    );
  };

  render() {

    let mainRegion, footerRegion;
    if (this._isMounted) {
      mainRegion = this.props.page.regions.main.map((widget, index) => (
                  <React.Fragment key={index}>
                    <ReactSafeHtml html={widget.content} />
                  </React.Fragment>
                ));
      footerRegion = this.props.page.regions.footer.map((widget, index) => (
                  <React.Fragment key={index}>
                    <ReactSafeHtml html={widget.content} />
                  </React.Fragment>
                ));
    }

    return (
      <React.Fragment>
        <Layout>
          <Header className="header">
            <div className="logo" />
            <Menu
              theme="dark"
              mode="horizontal"
              defaultSelectedKeys={['1']}
              style={{ lineHeight: '64px' }}
            >
            <Menu.Item key="1"><Link to="/">Home</Link></Menu.Item>
            </Menu>
          </Header>
          <Layout>
            <Sider width={200} style={{ background: '#fff' }}>
              <Menu
                mode="inline"
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
                  <Menu.Item key="1"><Link to="/pages">Pages</Link></Menu.Item>
                  <Menu.Item key="2"><Link to="/users">Users</Link></Menu.Item>
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
                <h2>{this.props.page.title}</h2>
                {mainRegion}
                <List/>
                <h3>Add article</h3>
                <Form/>
                <h3>API pages</h3>
                <Post/>
                {footerRegion}
              </Content>
            </Layout>
          </Layout>
        </Layout>
      </React.Fragment>
    )
  }
}

function mapStateToProps(state) {
  return {
    page: state.page
  };
}

export default connect(
  mapStateToProps,
  { getPageData }
)(Page);
