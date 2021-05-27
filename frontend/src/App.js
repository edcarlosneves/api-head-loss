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
        <div className='row mt-5'>
          <div className='col-md-3'>
            <input type='text' placeholder='Analysis Name...' />
          </div>
          <div className='col-md-3'>
            <input type='text' placeholder='Density...' />
          </div>
          <div className='col-md-3'>
            <input type='text' placeholder='Kinematic Viscosity...' />
          </div>
          <div className='col-md-3'>
            <input type='text' placeholder='Pipe Diameter...' />
          </div>
        </div>
        <div className='row mt-5'>
          <div className='col-md-3'>
            <input type='text' placeholder='Volumetric Flow Rate...' />
          </div>
          <div className='col-md-3'>
            <input type='text' placeholder='Pipe Material...' />
          </div>
          <div className='col-md-3'>
            <input type='text' placeholder='Material Condition...' />
          </div>
          <div className='col-md-3'>
            <input type='text' placeholder='Pipe Length...' />
          </div>
        </div>
        <div className='mt-3 mb-5'>
          <button type='button' className='btn btn-success'>
            Calculate Head Loss
          </button>
        </div>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Name</th>
              <th>Density</th>
              <th>Kinematic Viscosity</th>
              <th>Pipe Diameter</th>
              <th>Volumetric Flow Rate</th>
              <th>Material</th>
              <th>Pipe Length</th>
              <th>Head Loss</th>
            </tr>
          </thead>
          <tbody>
            {analyses.map(function (analysis, index) {
              return (
                <tr key={analysis.id}>
                  <td>{analysis.analysis_name}</td>
                  <td>{analysis.density}</td>
                  <td>{analysis.kinematic_viscosity.toExponential(3)}</td>
                  <td>{analysis.pipe_diameter}</td>
                  <td>{analysis.volumetric_flow_rate}</td>
                  <td>
                    {analysis.pipe_material} ({analysis.material_condition})
                  </td>
                  <td>{analysis.pipe_length}</td>
                  <td>{analysis.head_loss.toExponential(2)}</td>
                  <td>
                    <div className='btn-group'>
                      {/* <div className='row center-text'>
                      <div className='col-md-6'> */}
                      <button type='button' className='btn btn-danger btn-sm'>
                        D
                      </button>
                      {/* </div> */}
                      {/* <div className='col-md-6'> */}
                      <button type='button' className='btn btn-primary btn-sm'>
                        E
                      </button>
                      {/* </div>
                    </div> */}
                    </div>
                  </td>
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
