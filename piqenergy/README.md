## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
yarn run dev

# or start the server and open the app in a new browser tab
yarn run dev -- --open
```

## Building

To create a production version of your app:

```bash
yarn run build
```

You can preview the production build with `yarn run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.
