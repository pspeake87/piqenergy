<script>
	export let isOpen = false;
	export let closeModal = () => {};

	let data = { start: '', end: '', scenario_type: 'summer peak', num_scenarios: 1 };

	const submitForm = async () => {
		try {
			const response = await fetch('http://127.0.0.1:8000/simulations', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(data)
			});

			if (!response.ok) {
				throw new Error(`Error: ${response.statusText}`);
			}

			const result = await response.json();
			console.log('Success:', result);
			location.reload();
		} catch (error) {
			console.error('Error:', error);
		}
	};
</script>

{#if isOpen}
	<div class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
		<div class="w-full max-w-lg rounded-lg bg-white p-6 shadow-lg dark:bg-gray-800">
			<div class="flex items-center justify-between border-b pb-4 dark:border-gray-600">
				<h2 class="text-lg font-semibold text-gray-800 dark:text-gray-200">New Simulation Study</h2>
				<button
					on:click={closeModal}
					class="text-lg text-gray-600 hover:text-gray-800 dark:text-gray-400 dark:hover:text-gray-200"
				>
					&times;
				</button>
			</div>
			<div class="text-gray-600 dark:text-gray-300">
				<div class="mx-auto max-w-md rounded-lg bg-white p-6 dark:bg-gray-800">
					<form method="POST" on:submit|preventDefault={submitForm} class="space-y-4">
						<div>
							<label
								for="scenario"
								class="block text-sm font-medium text-gray-700 dark:text-gray-300"
								>Number of Scenarios</label
							>
							<input
								type="number"
								bind:value={data.num_scenarios}
								id="scenario"
								name="scenario"
								min="1"
								max="3"
								step="1"
								class="mt-1 block w-full rounded-md border-gray-300 bg-gray-50 text-gray-900 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm dark:border-gray-600 dark:bg-gray-700 dark:text-gray-100"
							/>
						</div>
						<div>
							<label for="type" class="block text-sm font-medium text-gray-700 dark:text-gray-300"
								>Scenario Type</label
							>
							<select
								id="type"
								name="type"
								bind:value={data.scenario_type}
								class="mt-1 block w-full rounded-md border-gray-300 bg-gray-50 text-gray-900 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm dark:border-gray-600 dark:bg-gray-700 dark:text-gray-100"
							>
								<option value="summer peak">Summer Peak</option>
								<option value="winter peak">Winter Peak</option>
								<option value="light load">Light Load</option>
							</select>
						</div>
						<div>
							<label for="start" class="block text-sm font-medium text-gray-700 dark:text-gray-300"
								>Start Date</label
							>
							<input
								type="date"
								id="start"
								name="start"
								bind:value={data.start}
								class="mt-1 block w-full rounded-md border-gray-300 bg-gray-50 text-gray-900 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm dark:border-gray-600 dark:bg-gray-700 dark:text-gray-100"
							/>
						</div>
						<div>
							<label for="end" class="block text-sm font-medium text-gray-700 dark:text-gray-300"
								>End Date</label
							>
							<input
								type="date"
								id="end"
								name="end"
								bind:value={data.end}
								class="mt-1 block w-full rounded-md border-gray-300 bg-gray-50 text-gray-900 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm dark:border-gray-600 dark:bg-gray-700 dark:text-gray-100"
							/>
						</div>
						<div>
							<button
								type="submit"
								class="w-full rounded-md bg-blue-600 px-4 py-2 text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 dark:focus:ring-offset-gray-800"
							>
								Run Simulation
							</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
{/if}
