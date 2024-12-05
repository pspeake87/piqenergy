import containerQueries from '@tailwindcss/container-queries';
import forms from '@tailwindcss/forms';
import typography from '@tailwindcss/typography';
import type { Config } from 'tailwindcss';

export default {
  content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/layerchart/**/*.{svelte,js}'],
  darkMode: 'class',

  theme: {
    extend: {}
  },

  plugins: [typography, forms, containerQueries]
} satisfies Config;
