import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
    const response = await fetch('http://127.0.0.1:8000/simulations?offset=0&limit=100', {
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