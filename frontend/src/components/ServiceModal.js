// frontend/src/components/Modal.js

import React from "react";
import {
  Modal,
  Form,
  Input,
  Checkbox,
} from 'antd';

const ServiceModalForm = Form.create({ name: 'form_in_modal' })(
  // eslint-disable-next-line
  class extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        checked: this.props.activeItem.completed,
        activeItem: this.props.activeItem
      }
    }
    
    onChange = e => {
      console.log('checked = ', e.target.checked);
      this.setState({
        checked: e.target.checked,
      });
    };
    render() {
      const { visible, onCancel, onCreate, form } = this.props;
      const { getFieldDecorator } = form;
      return (
        <Modal
          visible={visible}
          title="Service options"
          okText="OK"
          onCancel={onCancel}
          onOk={() => onCreate(this.state.activeItem)}
        >
          <Form layout="vertical">
            <Form.Item label="Name">
              {getFieldDecorator('name', {
                initialValue: this.state.activeItem.name,
                rules: [{ required: true}],
              })(<Input />)}
            </Form.Item>
            <Form.Item label="Link">
              {getFieldDecorator('link', {
                initialValue: this.state.activeItem.link,
                rules: [{ required: true}],
              })(<Input type="textarea" />)}
            </Form.Item>
            <Form.Item label="description">
              {getFieldDecorator('description', {
                initialValue: this.state.activeItem.description,
                rules: [{ required: false}],
              })(<Input type="textarea" />)}
            </Form.Item>
            <Form.Item className="collection-create-form_last-form-item">
              {getFieldDecorator('completed')(
                <Checkbox
                  checked={this.state.checked}
                  onChange={this.onChange}
                >
                  Completed
                </Checkbox>
              )}
            </Form.Item>
          </Form>
        </Modal>
      );
    }
  },
);

export default ServiceModalForm;
