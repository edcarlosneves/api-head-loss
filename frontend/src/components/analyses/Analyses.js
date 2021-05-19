import React, { useEffect, useContext } from 'react';
import HeadLossContext from '../../context/headloss/headLossContext';
import AnalysisItem from './AnalysisItem';

const Analyses = () => {
  const headLossContext = useContext(HeadLossContext);

  const { analyses, getAnalyses } = headLossContext;

  useEffect(() => {
    getAnalyses();
    // eslint-disable-next-line
  }, []);

  return analyses.map((analysis) => (
    <AnalysisItem repo={analysis} key={analysis.id} />
  ));
};

export default Analyses;
