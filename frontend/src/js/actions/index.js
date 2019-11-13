import {ADD_ARTICLE, DATA_LOADED} from "../constants/action-types";

export function addArticle(payload) {
  return { type: ADD_ARTICLE, payload }
}

// export function getData() {
//   return function(dispatch) {
//     return fetch("https://jsonplaceholder.typicode.com/posts")
//       .then(response => response.json())
//       .then(json => {
//         return { type: DATA_LOADED, payload: json };
//       });
//   }
// }

export function getData() {
  return function(dispatch) {
    return fetch("http://localhost:8000/api/pages/")
      .then(response => response.json())
      .then(json => {
        dispatch({ type: DATA_LOADED, payload: json });
      });
  };
}

export function getPageData(id) {
  return function(dispatch) {
    return fetch("http://localhost:8000/api/pages/" + id)
      .then(response => response.json())
      .then(json => {
        dispatch({ type: "PAGE_LOADED", payload: json });
      });
  };
}