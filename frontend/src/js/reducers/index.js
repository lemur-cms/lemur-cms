import {ADD_ARTICLE, DATA_LOADED} from "../constants/action-types";

const initialState = {
  articles: [],
  remoteArticles: [],
  page: []
};

function rootReducer(state = initialState, action) {
  if (action.type === ADD_ARTICLE) {
    return Object.assign({}, state, {
      articles: state.articles.concat(action.payload)
    })
  }
  if (action.type === DATA_LOADED) {
    return Object.assign({}, state, {
      remoteArticles: action.payload
    });
  }
  if (action.type === "PAGE_LOADED") {
    return Object.assign({}, state, {
      page: action.payload
    });
  }
  return state;
}

export default rootReducer;
