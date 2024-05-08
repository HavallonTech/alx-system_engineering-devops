# Fixing an apache file setting in a php environment

exec{ 'fix-wordpres':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
