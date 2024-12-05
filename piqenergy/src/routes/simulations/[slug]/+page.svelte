<script lang="ts">
	import type { PageData } from '../$types';
	import { LineChart } from 'layerchart';
	import { formatGraphData } from '../../../utils/data';
	let { data }: { data: PageData } = $props();

	const dataPoints = formatGraphData(data.data);
</script>

<div class="container mx-auto flex flex-row overflow-x-auto">
	<div
		class="h-[400px] w-full rounded border border-gray-200 bg-white p-6 shadow-md dark:border-gray-700 dark:bg-gray-800"
	>
		<LineChart
			props={{
				xAxis: {
					rule: { class: 'stroke-gray-400 dark:stroke-gray-500' },
					tickLabelProps: { class: 'fill-gray-600 dark:fill-gray-300 text-sm' }
				},
				yAxis: {
					rule: { class: 'stroke-gray-400 dark:stroke-gray-500' },
					tickLabelProps: { class: 'fill-gray-600 dark:fill-gray-300 text-sm' }
				},
				legend: {
					classes: { label: 'text-gray-800 dark:text-gray-200 font-medium text-sm' }
				}
			}}
			data={dataPoints.data}
			x="dt"
			series={dataPoints.series}
			legend
		/>
	</div>
</div>
