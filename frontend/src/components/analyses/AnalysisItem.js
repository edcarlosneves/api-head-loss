import React from 'react';
import PropTypes from 'prop-types';

const AnalysisItem = ({ analysis }) => {
  return (
    <div>
      <h3>{analysis.analysis_name}</h3>
    </div>
  );
};

export default AnalysisItem;
