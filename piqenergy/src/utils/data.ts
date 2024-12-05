type DataPoint = {
  id: number;
  created: string;
  dt: string;
  power_MW: number;
  scenario: number;
  simulation_id: string;
};

enum scenario {'Scenario 1', 'Scenario 2', 'Scenario 3'}

const colors = ['blue', 'red', 'green']

export function formatGraphData(array: DataPoint[]) {
    const newArray = array.map((item: DataPoint) => ({
		dt: new Date(item.dt),
		[scenario[item.scenario]]: item.power_MW
	}));

    const temp = [...new Set(array.map(obj => obj['scenario']))]

    const series = temp.map((item, index) => ({ key: scenario[item], color: colors[index] }))

    return { data: newArray, series };
}