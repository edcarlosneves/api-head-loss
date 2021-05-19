import { GET_ANALYSES } from '../types';

export default (state, action) => {
  switch (action.type) {
    case GET_ANALYSES: {
      return {
        ...state,
        analyses: action.payload,
        loading: false,
      };
    }
    default:
      return state;
  }
};
