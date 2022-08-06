<script>
    import { useForm, validators, HintGroup, Hint, email, required } from "svelte-use-form";
  
    const form = useForm();


    var password = "";
    var username =  "";


    async function Login () {
		  await fetch('http://127.0.0.1:8080/login', {
			  method: 'POST',
        credentials: 'include',
        mode: 'cors',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Credentials': 'true',
          'Content-Type': 'application/json',
          'withCredentials': 'true',
          'credentials': 'include'
        },
			  body: JSON.stringify({
			  	username: username,
			  	password: password
			  })
		  })
    }
    

</script>


<form id="form" use:form>
  <h1>Login</h1>

  <input bind:value={username} type="text" name="username" use:validators={[required]} />
  <Hint for="username" on="required">This is a mandatory field</Hint>

  <input bind:value={password} type="password" name="password" use:validators={[required]} />
  <Hint for="password" on="required">This is a mandatory field</Hint>

  <button type=“button” on:click={Login}>Login</button>
</form>

<style>
	:global(.touched:invalid) {
		border-color: red;
		outline-color: red;
	}
</style>