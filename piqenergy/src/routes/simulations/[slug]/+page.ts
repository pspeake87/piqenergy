import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch, params }) => {
    const response = await fetch(`http://127.0.0.1:8000/simulations/${params.slug}`, {
		method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    });
    
    if (!response.ok) {
        throw new Error('Failed to fetch data');
    }

    const data = await response.json();

    return {
        data
    };
};