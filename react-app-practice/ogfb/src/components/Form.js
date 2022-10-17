import React from 'react';

class Form extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'firstname': '',
            'lastname': '',
            'activity': '',
        }

        this.handleInput = this.handleInput.bind(this); // no longer necessary
    }

    componentDidMount() {
        // console.log('Form mounted');
        fetch('https://www.boredapi.com/api/activity')
            .then(response => response.json())
            .then(data => {
                this.setState({
                    'activity': data['activity']
                });
            }, (error) => {
                console.log(error);
            });
    }

    componentDidUpdate() {
        const name = this.state.firstname;
        fetch('https://api.agify.io?name=' + name)
            .then(response => response.json())
            .then(data => {
                this.setState({
                    'age': data['age']
                });
            })
    }

    handleInput = (event) => {
        // console.log(event.target.value);
        // console.log('name ' + event.target.name);

        const name = event.target.name;
        const value = event.target.value;

        this.setState({
            [name] : value
        });  // every time you add a value to state, you update -- every keystroke, event is logged and used

        console.log(this.state);
    }

    handleSubmit = (event) => {
        event.preventDefault();
        // alert('hello!');
        alert(this.state.firstname + ' ' + this.state.lastname + ' age: ' + this.state.age + ' just: ' + this.state.activity);
    }

    render() {
        return (
            <div className='form'>
                <h3>(this.props.name)</h3>
                <form onSubmit={this.handleSubmit}>
                    <form>
                        <input onChange={this.handleInput} type='text' placeholder='First Name' name='firstname'/>
                        <input type='text' placeholder='Last Name' name='lastname'/>
                        <input type='text' placeholder='{this.state.activity}' name='activity'/>
                        <input type='submit' value='Submit'/>
                    </form>
                </form>
            </div>
        )
    }
}

export default Form;
