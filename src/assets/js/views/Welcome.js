import { h } from 'preact';

const Welcome = () => (
  <div class="starter-template">
    <div class="container">
      <div uk-grid>
        <div class="uk-width-1-4" />
        <div class="uk-width-1-2">
          <div class="content">
            <h1>
              <span class="font-semi-bold">Pyramid</span> <span class="smaller">Alchemy project</span>
            </h1>
            <p class="lead">
              Welcome to <span class="font-normal">canopus</span>, a&nbsp;Pyramid application generated&nbsp;by<br />
              <span class="font-normal">Cookiecutter</span>.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
);

export default Welcome;
