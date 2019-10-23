import React from "react";
import { Responsive, WidthProvider, } from 'react-grid-layout';

const ResponsiveGridLayout = WidthProvider(Responsive);

class ResponsiveGrid extends React.Component {
  onLoad = () => {
    this.forceUpdate();
  };
  render() {
    return (
      <ResponsiveGridLayout className="layout" breakpoints={{lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}}
        cols={{lg: 12, md: 12, sm: 6, xs: 6, xxs: 6}} rowHeight={60}>
        <div key="a" className="page-widget" data-grid={{x: 0, y: 0, w: 12, h: 1}}>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eget finibus risus. Pellentesque in augue lacus. Ut faucibus placerat urna, nec mollis sapien viverra non. Aenean in molestie diam. Vestibulum a gravida odio, id elementum dui. In hac habitasse platea dictumst. Duis bibendum vehicula sapien, at semper eros sagittis imperdiet. Aenean venenatis lacus eget tempor feugiat. Quisque sagittis facilisis lorem sed dictum. Pellentesque aliquet enim eu odio finibus condimentum. Nam congue non dolor quis fermentum. Vestibulum ornare turpis vitae nibh imperdiet placerat. Ut at tempor felis.

Phasellus quis eros vel velit rutrum ultricies non quis nisi. Duis condimentum lacus nec arcu venenatis accumsan. Phasellus vestibulum ultricies velit non posuere. Ut at tortor vulputate, fringilla arcu lacinia, interdum ante. Vestibulum vulputate est et varius lacinia. Cras id nisl ac erat auctor scelerisque ut ac nulla. Donec luctus dapibus nulla, vel accumsan lorem molestie eget. Aenean feugiat porttitor feugiat. Nam sodales posuere purus, nec vestibulum lorem consectetur a. Donec euismod elit et blandit interdum.

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam pulvinar tellus vitae lectus placerat ornare. Integer dolor turpis, porttitor non pharetra at, laoreet at purus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam vel vulputate tellus. Vivamus lacinia dolor tempor, mattis eros sit amet, accumsan diam. Duis hendrerit ut ipsum vitae convallis. Sed elit tortor, mattis vel tortor laoreet, pulvinar dignissim velit. Duis consectetur pellentesque sapien dictum auctor.

Aliquam lectus nulla, consequat eu vehicula ut, vehicula at nisl. Fusce quis commodo tellus, non luctus eros. Pellentesque elementum ligula arcu, vel varius tellus commodo quis. Suspendisse convallis velit vitae scelerisque aliquet. Aenean metus urna, efficitur sed convallis a, pharetra eu dolor. Vivamus facilisis feugiat tortor vitae dictum. Aliquam nisi neque, dapibus rutrum enim id, faucibus vulputate nunc. Aliquam quis lobortis tellus, id posuere sapien.

Vivamus efficitur posuere erat, quis tincidunt sem tempor a. Nam viverra tu</p>
        </div>
        <div key="b" className="page-widget" data-grid={{x: 1, y: 0, w: 3, h: 2, minW: 2}}>b</div>
        <div key="c" className="page-widget" data-grid={{x: 4, y: 0, w: 5, h: 3}}>

        </div>
      </ResponsiveGridLayout>
    )
  }
}

export default ResponsiveGrid;
