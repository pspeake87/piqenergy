<script lang="ts">
	export const ssr = false;
	import '../app.css';
	let { children } = $props();

	let isDarkMode = $state(false);

	const toggleDarkMode = () => {
		isDarkMode = !isDarkMode;
		if (isDarkMode) {
			document.documentElement.classList.add('dark');
		} else {
			document.documentElement.classList.remove('dark');
		}
	};
</script>

<header class="bg-gray-100 shadow-md dark:bg-gray-800">
	<div class="container mx-auto flex items-center justify-between px-4 py-3">
		<!-- Logo -->
		<a href="/" class="flex items-center space-x-4">
			<span class="text-xl font-semibold text-gray-800 dark:text-gray-200">Piq Energy</span>
		</a>

		<!-- Navigation Links -->
		<nav class="hidden items-center space-x-6 md:flex">
			<a
				href="#about"
				class="text-gray-600 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400"
				>Example 1</a
			>
			<a
				href="#services"
				class="text-gray-600 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400"
				>Example 2</a
			>
			<a
				href="#contact"
				class="text-gray-600 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400"
				>Example 3</a
			>
		</nav>

		<!-- Dark Mode Toggle -->
		<button
			on:click={toggleDarkMode}
			class="flex h-10 w-10 items-center justify-center rounded-full bg-gray-200 text-gray-600 hover:bg-gray-300 dark:bg-gray-600 dark:text-gray-300 dark:hover:bg-gray-500"
			aria-label="Toggle Dark Mode"
		>
			{#if isDarkMode}
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					class="h-5 w-5"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-7.364l-.707.707M6.343 17.657l-.707.707m12.021 0l-.707-.707M6.343 6.343l-.707-.707"
					/>
				</svg>
			{:else}
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					class="h-5 w-5"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M12 2a9 9 0 100 18 9 9 0 000-18zm0 0v.01M21 12.01H21M12 21v-.01M3 12.01H3M18.36 5.64l-.01.01M5.64 18.36l-.01.01M16.24 16.24l-.01.01M7.76 7.76l-.01.01"
					/>
				</svg>
			{/if}
		</button>
	</div>
</header>

<div class="min-h-screen w-full p-12 dark:bg-gray-900">
	{@render children()}
</div>
