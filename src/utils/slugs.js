export function createProductSlug(name) {
  if (!name) return '';
  return name
    .toString()
    .toLowerCase()
    .trim()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '') // Elimina tildes y diacríticos
    .replace(/[^a-z0-9]+/g, '-')     // Reemplaza caracteres especiales y espacios por guiones
    .replace(/^-+|-+$/g, '');        // Elimina guiones iniciales y finales
}
