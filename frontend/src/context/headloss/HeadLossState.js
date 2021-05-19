import React, { useReducer } from 'react';
import axios from 'axios';
import HeadLossContext from './headLossContext';
import HeadLossReducer from './headLossReducer';
import { GET_ANALYSES } from '../types';

const HeadLossState = (props) => {
  const initialState = {
    analyses: [],
    loading: false,
  };

  const [state, dispatch] = useReducer(HeadLossReducer, initialState);

  // Get Analyses
  const getAnalyses = async () => {
    const res = await axios.get('http://localhost:8000/api/analysis/');

    dispatch({
      type: GET_ANALYSES,
      payload: res,
    });
  };

  return (
    <HeadLossContext.Provider value={{ analyses: state.analyses, getAnalyses }}>
      {props.children}
    </HeadLossContext.Provider>
  );
};

export default HeadLossState;
