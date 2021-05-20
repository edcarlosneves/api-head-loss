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
              <th>Pipe Material</th>
              <th>Material Condition</th>
              <th>Pipe Length</th>
              <th>Head Loss</th>
            </tr>
          </thead>
          <tbody>
            {analyses.map(function (analysis, index) {
              return (
                <tr key={index}>
                  <td>{index + 1}</td>
                  <td>{analysis.analysis_name}</td>
                  <td>{analysis.density}</td>
                  <td>{analysis.kinematic_viscosity.toExponential(3)}</td>
                  <td>{analysis.pipe_diameter}</td>
                  <td>{analysis.volumetric_flow_rate}</td>
                  <td>{analysis.pipe_material}</td>
                  <td>{analysis.material_condition}</td>
                  <td>{analysis.pipe_length}</td>
                  <td>{analysis.head_loss.toExponential(2)}</td>
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
