const LightsOffLight = React.createClass({
  _handleClick() {
    const {rowIndex, index} = this.props;
    this.props.onClick(rowIndex, index)
  },

  render() {
    const {on} = this.props;

    return (
      <div onClick={this._handleClick} className={"lights-off-light " + (on ? 'on' : 'off')}/>
    );
  }
});

const LightsOffRow = React.createClass({
  render() {
    const {lights, handleClick} = this.props;
    return (
      <div className="lights-off-row">
        {lights.map((light, index) => {
          return <LightsOffLight {...light} index={index} key={index} onClick={handleClick}/>
        })}
      </div>
    );
  }
});

const LightsOffGrid = React.createClass({
  getInitialState() {
    return { lightRows: [] }
  },


  componentDidMount() {
    const {numLightsX, numLightsY} = this.props;
    console.log(numLightsX)
    console.log(numLightsY)
    this._setupGrid(numLightsX, numLightsY);
  },

  componentDidRecieveProps(newProps) {
    const {numLightsX, numLightsY} = newProps;
    this._setupGrid(numLightsX, numLights);
  },

  _setupGrid(numLightsX, numLightsY, lightsOff) {
    let lightRows = [];

    for (let x = 0; x < numLightsX; x++) {
      let newRow = [];
      for (let y = 0; y < numLightsY; y++) {
        newRow.push({on: Math.random() < 0.5, rowIndex: x});
      }

      lightRows.push(newRow);
    }

    this.setState({lightRows: lightRows});
  },

  _checkBounds(xIndex, yIndex) {
    const {numLightsX, numLightsY} = this.props;
    return xIndex >= 0 &&
           yIndex >= 0 &&
           xIndex < numLightsX &&
           yIndex < numLightsY;
  },

  _toggleLight(lightRows, xIndex, yIndex) {
    if (this._checkBounds(xIndex, yIndex)) {
      lightRows[xIndex][yIndex].on = !lightRows[xIndex][yIndex].on
    }
    return lightRows;
  },

  _handleLightClick(xIndex, yIndex) {
    console.log(xIndex)
    console.log(yIndex)
    let {lightRows} = this.state
    lightRows = this._toggleLight(lightRows, xIndex, yIndex);
    lightRows = this._toggleLight(lightRows, xIndex-1, yIndex);
    lightRows = this._toggleLight(lightRows, xIndex+1, yIndex);
    lightRows = this._toggleLight(lightRows, xIndex, yIndex-1);
    lightRows = this._toggleLight(lightRows, xIndex, yIndex+1);

    this.setState({lightRows: lightRows});
  },

  render() {
    const {lightRows} = this.state
    console.log(lightRows)
    return (
      <div>
        {lightRows.map((row, index) => {
          return <LightsOffRow lights={row} index={index} key={index} handleClick={this._handleLightClick}/>
        })}
      </div>
    );
  }
});


React.render(<LightsOffGrid numLightsX={5} numLightsY={5}/>, document.getElementById('app'));
