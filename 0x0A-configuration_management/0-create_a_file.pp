#Using Puppet puppet script to create a file
file { '/tmp/school':
  ensure  => 'present',
  path    => '/tmp/school',
  group   => 'www-data',
  content => 'I love Puppet',
  owner   => 'www-data',
  mode    => '0744'
}
