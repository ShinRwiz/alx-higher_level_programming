#include "lists.h"
/**
 * reverse_listint --
 * @head: --
 * Return: --
 */
void reverse_listint(listint_t **head)
{
	listint_t *last = NULL;
	listint_t *next = NULL;
	listint_t *now = *head;

	while (now)
	{
		next = now->next;
		now->next = last;
		last = now;
		now = next;
	}
	*head = last;
}
/**
 * is_palindrome --
 * @head: --
 * Return: --
 */
int is_palindrome(listint_t **head)
{
	listint_t *go_1 = *head, *go_2 = *head;
	listint_t *clone = NULL, *temp = *head;

	if ((*head)->next == NULL || *head == NULL || head == NULL)
		return (1);

	while (1)
	{
		go_2 = go_2->next->next;
		if (!go_2)
		{
			clone = go_1->next;
			break;
		}
		if (!go_2->next)
		{
			clone = go_1->next->next;
			break;
		}
		go_1 = go_1->next;
	}
	reverse_listint(&clone);
	while (clone && temp)
	{
		if (temp->n == clone->n)
		{
			clone = clone->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!clone)
		return (1);

	return (0);
}
