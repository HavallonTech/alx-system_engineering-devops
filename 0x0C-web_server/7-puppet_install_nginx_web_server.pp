utomating puppet installation
package {''nginx':
  ensure =>'present',
  path => ''/etc/nginx/sites-enabled/default',
  after => 'listen 80 default_server;',
  line => 'rewrite ^/redirect_me https://youtube.com permanent;',
}
file {'/var/www/html/index.html':
  content => 'Hello World!',
}
service { 'nginx':
  ensure => running,
  require => package['nginx'],
}
