// frontend/src/App.js

import React, { Component } from "react";
import ServiceModalForm from "./js/components/ServiceModal";
import axios from "axios";

import {
  Row,
  Col,
  Button,
  List,
} from 'antd';

class ServiceApp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      activeItem: {},
      serviceList: [],
      visibleModal: false,
      serviceLoading: true,
      serviceReversedOrder: false,
    };
  }
  showModal = () => {
    this.setState({visibleModal: true})
  };
  handleCancel = () => {
    this.setState({visibleModal: false})
  };
  saveFormRef = formRef => {
    this.formRef = formRef;
  };
  componentDidMount() {
    this.refreshList();
    this.setState({visibleGrids: true})
  }
  refreshList = () => {
    axios
      .get(`http://localhost:8000/api/pages/`)
      .then(res => this.setState({ serviceList: res.data, serviceLoading: false}))
      .catch(err => console.log(err));
  };
  displayCompleted = status => {
    this.setState({serviceLoading: true})
    axios
      .get(`http://localhost:8000/api/pages/?parent=${this.state.viewCompleted ? '' : '3'}`)
      .then(res => this.setState({ serviceList: res.data, serviceLoading: false}))
      .catch(err => console.log(err));
    if (status) {
      return this.setState({ viewCompleted: true });
    }
    return this.setState({ viewCompleted: false });
  };
  renderTabList = () => {
    return (
        <Row>
          <Col>
            <Button
              onClick={() => this.displayCompleted(true)}
              className={this.state.viewCompleted ? "active" : ""}
            >
              complete
            </Button>
            <Button type="secondary"
              onClick={() => this.displayCompleted(false)}
              className={this.state.viewCompleted ? "" : "active"}
            >
              Incomplete
            </Button>
          </Col>
        </Row>
    );
  };
  renderItems = () => {
    return <List
      bordered
      loading={this.state.serviceLoading}
      dataSource={this.state.serviceList}
      renderItem={item => (
        <List.Item>
          <Col span={12}>
            <h3>{item.title}</h3>
            {/* {item.regions.map((item) =>
              <p>Blah{item.text}</p>
            )} */}
          </Col>
          <Col span={6}>
            <Button type="default" onClick={() => this.editItem(item)}>
              Edit
            </Button>
            <Button type="danger" onClick={() => this.handleDelete(item)}>
              Delete{" "}
            </Button>
          </Col>
        </List.Item>
      )}
    />
  };
  handleSubmit = item => {
    const { form } = this.formRef.props;
    form.validateFields((err, values) => {
      if (err)
        return;
      if (item.id) {
        axios
          .put(`http://localhost:8000/api/pages/${item.id}/`, values)
          .then(res => this.refreshList());
      } else {
        axios
          .post("http://localhost:8000/api/pages/", values)
          .then(res => this.refreshList());
      }
      form.resetFields();
      this.setState({ visibleModal: false });
    });
  };
  handleDelete = item => {
    axios
      .delete(`http://localhost:8000/api/pages/${item.id}`)
      .then(res => this.refreshList());
  };
  editItem = (item) => {
    this.setState({activeItem: item});
    this.showModal();
  };
  createItem = () => {
    const item = { title: "", link: "www.", description: "", completed: false };
    this.setState({ activeItem: item });
    this.showModal();
  };
  reverseServiceOrder = () => {
    this.setState({ serviceList: this.state.serviceList.reverse() })
  };
  render() {
    return (
      <div>
        <Row gutter={[24, 0]}>
          <Col span={24}>
            <h1>Service app - {this.state.serviceList.length}</h1>
            <Button type="primary" onClick={this.createItem}>
              Add service
            </Button>
            <Button type="default" onClick={this.reverseServiceOrder}>
              Reverse order
            </Button>
          </Col>
          <Col span={24}>
            {this.renderTabList()}
            {this.renderItems()}
          </Col>
        </Row>
        {this.state.visibleModal ? (
          <ServiceModalForm
            wrappedComponentRef={this.saveFormRef}
            visible={this.state.visibleModal}
            onCancel={this.handleCancel}
            onCreate={this.handleSubmit}
            activeItem={this.state.activeItem}
          />
        ) : null}
      </div>
    );
  }
}
export default ServiceApp;
