<script>
// @ts-nocheck
    import svelteLogo from '../assets/svelte.svg'
    import Counter from '../lib/Counter.svelte'
    import Bar from './Bar.svelte';
    import { modal } from './stores.js';
    import Modal from './Modal.svelte';

    let stickToTop = true;
</script>

<main>
  <Modal show={$modal}>
    <Bar {stickToTop}>
      here write all site code
    </Bar>
  </Modal>
</main>

  <style>
    .logo {
      height: 6em;
      padding: 1.5em;
      will-change: filter;
    }
    .logo:hover {
      filter: drop-shadow(0 0 2em #646cffaa);
    }
    .logo.svelte:hover {
      filter: drop-shadow(0 0 2em #ff3e00aa);
    }
    .read-the-docs {
      color: #888;
    }
</style>