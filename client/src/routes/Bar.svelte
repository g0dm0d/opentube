<script>
// @ts-nocheck

    import { getContext } from 'svelte';
    import sticky from './sticky.js';
    import Login from './Login.svelte'

    export let stickToTop = true;

    let isStuck = false;

    function handleStuck(e) {
        isStuck = e.detail.isStuck;
    }

    const showPopup = () => {
		open(Login);
	};
    const { open } = getContext('simple-modal');


    export let query;


    let result = null
	fetch('http://127.0.0.1:8080/@me', {
		method: 'GET',
        credentials: 'same-origin',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'withCredentials': 'true',
            'credentials': 'include'
        }
	})
</script>

<section>
    {#if !stickToTop}
        <slot />
    {/if}

    <h2
        class="sticky"
        class:isStuck
        data-position={stickToTop ? 'top' : 'bottom'}
        use:sticky={{ stickToTop }}
        on:stuck={handleStuck}>

        <input bind:value={query} class="search-input" type="search"placeholder="Search" />
        <button on:click={showPopup}>Login</button>
    </h2>

    {#if stickToTop}
        <slot />
    {/if}
</section>

<style>
    h2 {
        margin: 0;
    }

    .sticky {
        position: sticky;
        padding: 1rem;
        background: #181818;
        transition: all 0.3s;
    }

    .sticky[data-position='top'] {
        top: 1rem;
    }

    .sticky[data-position='bottom'] {
        bottom: 1rem;
    }

    .sticky.isStuck {
        background: #181818;
        box-shadow: 0px 0px 1px 0px rgba(0, 0, 0, 0.2),
            0px 0px 6px 0px rgba(0, 0, 0, 0.3);
    }

    section {
        border-radius: 5px;
        padding: 0.5rem;
        margin-bottom: 1rem;
    }

    .search-input {
      width: 100%;
      max-width: 800px;
      border-radius: 4px;
      border: 1px solid #ccc;
      padding: 10px 20px;
      font-size: 20px;
    }
</style>