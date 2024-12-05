<script lang="ts">
	import type { PageData } from './$types';
	import { formatDate } from '../utils/dates';
	import Modal from '../components/Modal.svelte';

	let { data }: { data: PageData } = $props();

	const simulations = data.data;

	let isModalOpen = $state(false);

	const openModal = () => {
		isModalOpen = true;
	};

	const closeModal = () => {
		isModalOpen = false;
	};
</script>

<div class="container mx-auto mb-8 flex items-center justify-between overflow-x-auto">
	<h1 class="mb-4 text-2xl font-bold text-gray-800 dark:text-gray-100">Simulations</h1>
	<button
		onclick={openModal}
		class="mr-2 rounded-lg bg-blue-600 px-6 py-2 text-sm font-medium text-white shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 dark:focus:ring-offset-gray-800"
	>
		New Simulation
	</button>
</div>

<div class="overflow-x-auto">
	<table
		class="container mx-auto table-auto text-gray-800 shadow-md dark:bg-gray-800 dark:text-gray-200"
	>
		<thead>
			<tr class="bg-gray-100 dark:bg-gray-700">
				<th class="border-b px-4 py-2 text-gray-800 dark:border-gray-600 dark:text-gray-200"
					>Date Created</th
				>
				<th class="border-b px-4 py-2 text-gray-800 dark:border-gray-600 dark:text-gray-200"
					># of Scenarios</th
				>
				<th class="border-b px-4 py-2 text-gray-800 dark:border-gray-600 dark:text-gray-200"></th>
			</tr>
		</thead>
		<tbody>
			{#each simulations as item}
				<tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
					<td class="border-b px-4 py-2 text-gray-800 dark:border-gray-600 dark:text-gray-200"
						>{formatDate(item.created_at)}</td
					>
					<td class="border px-4 py-2 text-gray-800 dark:border-gray-600 dark:text-gray-200"
						>{item.num_scenarios}</td
					>
					<td class="border-b px-4 py-2 text-gray-800 dark:border-gray-600 dark:text-gray-200"
						><a href={`/simulations/${item.id}`} class="underline">View</a></td
					>
				</tr>
			{/each}
		</tbody>
	</table>

	<Modal isOpen={isModalOpen} {closeModal} />
</div>
