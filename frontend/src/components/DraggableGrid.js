import React from 'react';
import GridDraggable, {Section} from 'grid-draggable';
import PropTypes from 'prop-types';
import Motion from "react-motion/lib/Motion";
import spring from "react-motion/lib/spring";
import { config } from 'react-spring'

class DraggableGrid extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <GridDraggable
        lg={4}
        md={3}
        xs={6}
        rowClassName="row-test"
        colClassName="page-widget">
        <Section
          key={1}
          style={{width: '100%', height: '100%'}}
          handle=".handle" // set handler
          dragClassName="dragging">
          {({dragging, match}) => {
            if (match) return ( // when match return <div/>
              <div style={{color: 'red'}}>This is a match</div>
            );

            // create a react-motion animation, when dragging using animations.
            const motionStyle = dragging
            ? {
                scale: spring(1.1, config.default),
                shadow: spring(16, config.default)
              }
            : {
                scale: spring(1, config.default),
                shadow: spring(1, config.default)
              };

            return (
              <Motion style={motionStyle}>
                {({scale, shadow}) => (
                    <div
                      style={{
                        boxShadow: `rgba(0, 0, 0, 0.2) 0px ${shadow}px ${2 * shadow}px 0px`,
                        transform: `translate3d(0, 0, 0) scale(${scale})`,
                        WebkitTransform: `translate3d(0, 0, 0) scale(${scale})`,
                      }}>
                      <div>
                        <p>aha</p>
                        <button className="handle">Click me to drag</button>
                      </div>
                    </div>
                  )
                }
              </Motion>
            );
          }}
        </Section>
        <Section
          key={2}
          style={{width: '100%', height: '100%'}}
          handle=".handle" // set handler
          dragClassName="dragging">
          {({dragging, match}) => {
            if (match) return ( // when match return <div/>
              <div style={{color: 'red'}}>This is a match</div>
            );

            // create a react-motion animation, when dragging using animations.
            const motionStyle = dragging
            ? {
                scale: spring(1.1, config.default),
                shadow: spring(16, config.default)
              }
            : {
                scale: spring(1, config.default),
                shadow: spring(1, config.default)
              };

            return (
              <Motion style={motionStyle}>
                {({scale, shadow}) => (
                    <div
                      style={{
                        boxShadow: `rgba(0, 0, 0, 0.2) 0px ${shadow}px ${2 * shadow}px 0px`,
                        transform: `translate3d(0, 0, 0) scale(${scale})`,
                        WebkitTransform: `translate3d(0, 0, 0) scale(${scale})`,
                      }} className="handle">
                      <div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eget finibus risus. Pellentesque in augue lacus. Ut faucibus placerat urna, nec mollis sapien viverra non. Aenean in molestie diam. Vestibulum a gravida odio, id elementum dui. In hac habitasse platea dictumst. Duis bibendum vehicula sapien, at semper eros sagittis imperdiet. Aenean venenatis lacus eget tempor feugiat. Quisque sagittis facilisis lorem sed dictum. Pellentesque aliquet enim eu odio finibus condimentum. Nam congue non dolor quis fermentum. Vestibulum ornare turpis vitae nibh imperdiet placerat. Ut at tempor felis.

Phasellus quis eros vel velit rutrum ultricies non quis nisi. Duis condimentum lacus nec arcu venenatis accumsan. Phasellus vestibulum ultricies velit non posuere. Ut at tortor vulputate, fringilla arcu lacinia, interdum ante. Vestibulum vulputate est et varius lacinia. Cras id nisl ac erat auctor scelerisque ut ac nulla. Donec luctus dapibus nulla, vel accumsan lorem molestie eget. Aenean feugiat porttitor feugiat. Nam sodales posuere purus, nec vestibulum lorem consectetur a. Donec euismod elit et blandit interdum.

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam pulvinar tellus vitae lectus placerat ornare. Integer dolor turpis, porttitor non pharetra at, laoreet at purus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam vel vulputate tellus. Vivamus lacinia dolor tempor, mattis eros sit amet, accumsan diam. Duis hendrerit ut ipsum vitae convallis. Sed elit tortor, mattis vel tortor laoreet, pulvinar dignissim velit. Duis consectetur pellentesque sapien dictum auctor.</p>
                      </div>
                    </div>
                  )
                }
              </Motion>
            );
          }}
        </Section>
      </GridDraggable>
    );
  }
}

export default DraggableGrid;