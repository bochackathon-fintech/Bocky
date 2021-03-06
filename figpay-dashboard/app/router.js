import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function () {
  this.route('history');
  this.route('analytics');
  this.route('account');
  this.route('login');

});

export default Router;
