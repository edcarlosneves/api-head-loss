import React from 'react';
import { Container, Table } from 'react-bootstrap';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Navbar from './components/layout/Navbar';
import About from './components/pages/About';
import Home from './components/pages/Home';

import HeadLossState from './context/headloss/HeadLossState';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      Analyses: [],
    };
    this.fetchTasks = this.fetchTasks.bind(this);
  }

  componentWillMount() {
    this.fetchTasks();
  }

  fetchTasks() {
    fetch('http://localhost:8000/api/analysis/')
      .then((response) => response.json())
      .then((data) =>
        this.setState({
          Analyses: data,
        })
      );
  }

  render() {
    var analyses = this.state.Analyses;
    console.log(analyses);
    return (
      <Container>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>#</th>
              <th>Analysis Name</th>
              <th>Densisty</th>
              <th>Kinematic Viscosity</th>
              <th>Pipe Diameter</th>
              <th>Volumetric Flow Rate</th>
            </tr>
          </thead>
          <tbody>
            {analyses.map(function (analysis, index) {
              return (
                <tr key={index}>
                  <td>{index + 1}</td>
                  <td>{analysis.analysis_name}</td>
                  <td>{analysis.density}</td>
                  <td>{analysis.kinematic_viscosity}</td>
                  <td>{analysis.pipe_diameter}</td>
                  <td>{analysis.volumetric_flow_rate}</td>
                </tr>
              );
            })}
          </tbody>
        </Table>
      </Container>
    );
  }
}

export default App;
