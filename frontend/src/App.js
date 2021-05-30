import React from 'react';
import { Container, Table, Navbar } from 'react-bootstrap';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

// import Navbar from './components/layout/Navbar';
// import About from './components/pages/About';
// import Home from './components/pages/Home';

import HeadLossState from './context/headloss/HeadLossState';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      Analyses: [],
      activeItem: {
        id: null,
        analysis_name: '',
        density: '',
        kinematic_viscosity: '',
        pipe_diameter: '',
        volumetric_flow_rate: '',
        pipe_material: '',
        material_condition: '',
        pipe_length: '',
        owner: 1,
        username: '',
        password: '',
      },
      editing: false,
    };
    this.getToken = this.getToken.bind(this);
    this.fetchTasks = this.fetchTasks.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleLogout = this.handleLogout.bind(this);
  }

  getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + '=') {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  componentWillMount() {
    this.fetchTasks();
  }

  getToken(e) {
    e.preventDefault();

    var csrftoken = this.getCookie('csrftoken');

    fetch('http://localhost:8000/api-token-auth/', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify(this.state.activeItem),
    })
      .then((response) => response.json())
      .then((data) => localStorage.setItem('user_token', data['token']))
      .then(this.fetchTasks);
  }

  fetchTasks() {
    var user_token = localStorage.getItem('user_token');

    console.log('token: ' + user_token);
    fetch('http://localhost:8000/api/analysis/', {
      headers: {
        Authorization: 'Token ' + user_token,
      },
    })
      .then((response) => response.json())
      .then((data) =>
        this.setState({
          Analyses: data,
        })
      );
  }

  deleteItem(analysis) {
    var csrftoken = this.getCookie('csrftoken');

    var user_token = localStorage.getItem('user_token');

    fetch(`http://localhost:8000/api/analysis/${analysis.id}/`, {
      method: 'DELETE',
      headers: {
        'Content-type': 'application/json',
        'X-CSRFToken': csrftoken,
        Authorization: 'Token ' + user_token,
      },
    }).then((response) => {
      this.fetchTasks();
    });
  }

  handleChange(e) {
    var name = e.target.name;
    var value = e.target.value;
    console.log('Name:', name);
    console.log('Value:', value);

    this.setState({
      activeItem: {
        ...this.state.activeItem,
        owner: 1,
        [name]: e.target.value,
      },
    });
  }

  startEdit(analysis) {
    this.setState({
      activeItem: analysis,
      editing: true,
    });
  }

  handleSubmit(e) {
    e.preventDefault();
    // console.log('ITEM:', this.state.activeItem);

    var csrftoken = this.getCookie('csrftoken');

    var url = 'http://localhost:8000/api/analysis/';

    var user_token = localStorage.getItem('user_token');

    var method = 'POST';

    if (this.state.editing === true) {
      url = `http://localhost:8000/api/analysis/${this.state.activeItem.id}/`;
      method = 'PUT';
      this.setState({
        editing: false,
      });
    } else {
    }

    console.log(this.state.activeItem);

    fetch(url, {
      method: method,
      headers: {
        'Content-type': 'application/json',
        'X-CSRFToken': csrftoken,
        Authorization: 'Token ' + user_token,
      },
      body: JSON.stringify(this.state.activeItem),
    })
      .then((response) => {
        this.fetchTasks();
        this.setState({
          activeItem: {
            id: null,
            analysis_name: '',
            density: '',
            kinematic_viscosity: '',
            pipe_diameter: '',
            volumetric_flow_rate: '',
            pipe_material: '',
            material_condition: '',
            pipe_length: '',
            owner: 1,
          },
        });
      })
      .catch(function (error) {
        console.log('ERROR:', error);
      });
  }

  handleLogout(e) {
    e.preventDefault();
    localStorage.setItem('user_token', '');
    this.fetchTasks();
  }

  render() {
    var analyses = this.state.Analyses;
    var self = this;
    var user_token = localStorage.getItem('user_token');
    console.log('user_token: ' + user_token);
    if (user_token === '' || user_token === null) {
      return (
        <Container>
          <form onSubmit={this.getToken} id='form'>
            <div className='row mt-5'>
              <div className='col-md-3'>
                <input
                  type='text'
                  placeholder='Username...'
                  id='username'
                  value={this.state.username}
                  onChange={this.handleChange}
                  className='form-control'
                  name='username'
                />
              </div>
              <div className='col-md-3'>
                <input
                  type='password'
                  placeholder='Password...'
                  id='password'
                  value={this.state.password}
                  onChange={this.handleChange}
                  className='form-control'
                  name='password'
                />
              </div>
              <div className='col-md-3'>
                <input
                  id='submit'
                  type='submit'
                  className='btn btn-success'
                  name='login'
                  value='Login'
                />
              </div>
            </div>
          </form>
        </Container>
      );
    } else {
      return (
        <Container>
          <Navbar>
            <form onSubmit={this.handleLogout} id='logout-form'>
              <input
                id='submit'
                type='submit'
                className='btn btn-danger'
                name='logout'
                value='Logout'
              />
            </form>
          </Navbar>
          <form onSubmit={this.handleSubmit} id='form'>
            <div className='row mt-5'>
              <div className='col-md-3'>
                <input
                  type='text'
                  placeholder='Analysis Name...'
                  id='analysis_name'
                  value={this.state.activeItem.analysis_name}
                  onChange={this.handleChange}
                  className='form-control'
                  name='analysis_name'
                />
              </div>
              <div className='col-md-3'>
                <input
                  type='text'
                  placeholder='Density...'
                  id='density'
                  value={this.state.activeItem.density}
                  onChange={this.handleChange}
                  className='form-control'
                  name='density'
                />
              </div>
              <div className='col-md-3'>
                <input
                  type='text'
                  placeholder='Kinematic Viscosity...'
                  id='kinematic_viscosity'
                  value={this.state.activeItem.kinematic_viscosity}
                  onChange={this.handleChange}
                  className='form-control'
                  name='kinematic_viscosity'
                />
              </div>
              <div className='col-md-3'>
                <input
                  type='text'
                  placeholder='Pipe Diameter...'
                  id='pipe_diameter'
                  value={this.state.activeItem.pipe_diameter}
                  onChange={this.handleChange}
                  className='form-control'
                  name='pipe_diameter'
                />
              </div>
            </div>
            <div className='row mt-5'>
              <div className='col-md-3'>
                <input
                  type='text'
                  placeholder='Volumetric Flow Rate...'
                  id='volumetric_flow_rate'
                  value={this.state.activeItem.volumetric_flow_rate}
                  onChange={this.handleChange}
                  className='form-control'
                  name='volumetric_flow_rate'
                />
              </div>
              <div className='col-md-3'>
                <input
                  type='text'
                  placeholder='Pipe Material...'
                  id='pipe_material'
                  value={this.state.activeItem.pipe_material}
                  onChange={this.handleChange}
                  className='form-control'
                  name='pipe_material'
                />
              </div>
              <div className='col-md-3'>
                <input
                  type='text'
                  placeholder='Material Condition...'
                  id='material_condition'
                  value={this.state.activeItem.material_condition}
                  onChange={this.handleChange}
                  className='form-control'
                  name='material_condition'
                />
              </div>
              <div className='col-md-3'>
                <input
                  type='text'
                  placeholder='Pipe Length...'
                  id='pipe_length'
                  value={this.state.activeItem.pipe_length}
                  onChange={this.handleChange}
                  className='form-control'
                  name='pipe_length'
                />
              </div>
            </div>
            <div className='mt-3 mb-5'>
              <input
                id='submit'
                type='submit'
                className='btn btn-success'
                value='Calculate Head Loss'
                name='calculate_head_loss'
              />
            </div>
          </form>
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
                        <button
                          onClick={() => self.deleteItem(analysis)}
                          className='btn btn-sm btn-outline-dark delete'
                          type='button'
                          // className='btn btn-danger btn-sm'
                        >
                          D
                        </button>
                        <button
                          type='button'
                          className='btn btn-primary btn-sm'
                          onClick={() => self.startEdit(analysis)}
                        >
                          E
                        </button>
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
}

export default App;
